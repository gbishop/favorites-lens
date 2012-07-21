#  favorites-lens

## Summary

A hack lens for unity that searches my Firefox bookmarks.

I built this using quickly. It directly accesses the places.sqlite file in the default Firefox profile.

I know there is already a bookmarks-lens but it doesn't produce the results in an order that suited me and it was written in C. So, I hacked this simple one. I imagined I'd need a cache or some other fanciness to make it responsive but this simple minded approach seems adequate so far.

## Installation

sudo quickly install ought to work but doesn't for me. I ended up doing

sudo python setup.py install

Logging out and back in seemed to be the most reliable method of making sure it runs correctly.

## License

Feel free to use this for any purpose.
