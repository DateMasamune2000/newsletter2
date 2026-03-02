import rich
from lxml import etree
from config import load_config

def main(argv):
    config = load_config(argv[0])

    rich.print("[bold blue]NEWSLETTER[/bold blue]")
    for feed in config["feeds"]:
        filename = config["cache"]["files"][feed["id"]]
        path = f"{config['cache']['dir']}/{filename}"
        pretty_print(path)

def pretty_print(filename):
    feedtree = None

    with open(filename, "r") as rss_feed:
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
        print("\n---\n")

if __name__ == "__main__":
    main()
