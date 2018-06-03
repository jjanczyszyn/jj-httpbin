# -*- coding: utf-8 -*-
# Copyright (c) 2018 Justyna Janczyszyn <justyna.janczyszyn@gmail.com>
#
# this file is part of the project "JJ HTTPBin Client" released under the "MIT" open-source license
import httpretty

from jj_httpbin import HttpBinClient


def test_httpbinclient_make_full_url_with_default():
    ("HttpBinClient.make_full_url() should generate the correct URL with "
     "the default base url")

    # Given that I have an HttpBinClient with the default base url
    client = HttpBinClient()

    # When I call .make_full_url()
    result = client.make_full_url('/ip')

    # Then it should return a string with the full url
    result.should.be.a(str)
    result.should.equal('https://httpbin.org/ip')


def test_httpbinclient_make_full_url_with_custom_url():
    ("HttpBinClient.make_full_url() should generate the correct URL with "
     "a custom base url")

    # Given that I have an HttpBinClient with a custom base url
    client = HttpBinClient("http://localhost:8080")

    # When I call .make_full_url()
    result = client.make_full_url('/ip')

    # Then it should return a string with the full url
    result.should.be.a(str)
    result.should.equal('http://localhost:8080/ip')
