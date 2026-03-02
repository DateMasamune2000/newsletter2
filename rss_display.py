import rich
from lxml import etree

def main(argv):
    demo()

def demo():
    feedtree = None

    with open("example_content.xml", "r") as rss_feed:
        feedtree = etree.fromstring(rss_feed.read().encode())
        for channel in feedtree:
            for channel_child in channel:
                if channel_child.tag == "title":
                    rich.print(f"[bold]* [yellow]{channel_child.text}[/yellow] [/bold]")
                elif channel_child.tag == "item":
                    for item_child in channel_child:
                        if item_child.tag == "title":
                            rich.print(f"\n[white] - [/white] [bold]{item_child.text}[/bold]")
                        elif item_child.tag == "link":
                            rich.print(f"   {item_child.text}")

if __name__ == "__main__":
    main()
