# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

'''
Unit tests for the Python Facebook Business SDK.

How to run:
    python -m facebook_business.test.dpa_docs
'''
import os
import sys
import json
from .docs_utils import *


class ProductGroupDocsTestCase(DocsTestCase):
    pass


class ProductFeedDocsTestCase(DocsTestCase):

    def setUp(self):
        product_catalog = self.create_product_catalog()
        DocsDataStore.set('dpa_catalog_id', product_catalog.get_id())
        product_feed = self.create_product_feed(product_catalog.get_id())
        DocsDataStore.set('dpa_feed_id', product_feed.get_id())

    def test_get_products(self):
        feed = ProductFeed(DocsDataStore.get('dpa_feed_id'))
        products = feed.get_products(fields=[
            Product.Field.title,
            Product.Field.price,
        ])
        if products:
            self.store_response(products)


class ProductAudienceDocsTestCase(DocsTestCase):
    pass


class ProductDocsTestCase(DocsTestCase):
    pass


class ProductCatalogDocsTestCase(DocsTestCase):

    def setUp(self):
        product_catalog = self.create_product_catalog()
        DocsDataStore.set('dpa_catalog_id', product_catalog.get_id())
        pixel = self.create_ads_pixel()
        DocsDataStore.set('pixel_id', pixel.get_id())

    def test_get_product_feeds(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        feeds = catalog.get_product_feeds()
        if feeds:
            self.store_response(feeds[0])

    def test_add_external_event_sources(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        response = catalog.add_external_event_sources(pixel_ids=[
            DocsDataStore.get('pixel_id'),
        ])
        self.store_response(response)

    def test_get_external_event_sources(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        sources = catalog.get_external_event_sources()
        self.store_response(sources)

    def test_remove_external_event_sources(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        response = catalog.remove_external_event_sources(pixel_ids=[
            DocsDataStore.get('pixel_id'),
        ])
        self.store_response(response)


class ProductSetDocsTestCase(DocsTestCase):

    def setUp(self):
        product_catalog = self.create_product_catalog()
        DocsDataStore.set('dpa_catalog_id', product_catalog.get_id())
        product_set = self.create_product_set(product_catalog.get_id())
        DocsDataStore.set('dpa_set_id', product_set.get_id())

    def test_get_product_groups(self):
        product_set = ProductSet(DocsDataStore.get('dpa_set_id'))
        product_groups = product_set.get_product_groups(fields=[
            Product.Field.title,
            Product.Field.price,
        ])
        self.store_response(product_groups)

    def test_get_products(self):
        product_set = ProductSet(DocsDataStore.get('dpa_set_id'))
        products = product_set.get_products(fields=[
            Product.Field.title,
            Product.Field.price,
        ])
        self.store_response(products)


class ProductFeedUploadErrorDocsTestCase(DocsTestCase):
    pass


if __name__ == '__main__':
    handle = open(DocsDataStore.get('filename'), 'w')
    handle.write('')
    handle.close()

    try:
        config_file = open('./autogen_docs_config.json')
    except IOError:
        print("No config file found, skipping docs tests")
        sys.exit()
    config = json.load(config_file)
    config_file.close()

    FacebookAdsApi.init(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
        config['adaccount_id'],
    )

    DocsDataStore.set('adaccount_id', config['adaccount_id'])
    DocsDataStore.set('adaccount_id_int', config['adaccount_id_int'])
    DocsDataStore.set('business_id', config['business_id'])
    DocsDataStore.set('ca_id', config['ca_id'])
    DocsDataStore.set('ca_id', config['ca_id'])
    DocsDataStore.set('dpa_catalog_id', config['dpa_catalog_id'])
    DocsDataStore.set('dpa_set_id', config['dpa_set_id'])
    DocsDataStore.set('dpa_feed_id', config['dpa_feed_id'])
    DocsDataStore.set('dpa_upload_id', config['dpa_upload_id'])
    DocsDataStore.set('as_user_id', config['as_user_id'])
    DocsDataStore.set('page_id', config['page_id'])
    DocsDataStore.set('pixel_id', config['pixel_id'])

    unittest.main()
