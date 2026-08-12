"""
This script contains all configurations for processing versions of pages in
other language.
"""


def domain(self, response, kingdom=None, phylum=None):

    # response.xpath("/*[@lang]/@lang").get()

    duck = dict()

    if kingdom:
        duck[f"{kingdom}"] = response.url

    if phylum:
        order = dict()

        yield from self.life(response, order)

        # if order:
        #     duck[f"{phylum}"] = {response.url: [order, Goose({'keep_footnotes': False}).extract(raw_html=response.body).cleaned_text]}
        # else:
        #     duck[f"{phylum}"] = {response.url: Goose({'keep_footnotes': False}).extract(raw_html=response.body).cleaned_text}

        if order:
            duck[f"{phylum}"] = {response.url: order}
        else:
            duck[f"{phylum}"] = response.url

    yield duck
