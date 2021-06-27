import time
from urllib.request import urlopen


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content


def main() -> None:
    webpage = WebPage("https://estraviz.github.io")
    start = time.time()
    content1 = webpage.content
    print(time.time() - start)

    start = time.time()
    content2 = webpage.content
    print(time.time() - start)


if __name__ == '__main__':
    main()
