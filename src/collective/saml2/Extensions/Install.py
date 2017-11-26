def uninstall(portal):
    productname = 'dm.zope.saml2'

    sm = portal.getSiteManager()

    adapters = sm.utilities._adapters
    for x in adapters[0].keys():
        if x.__module__.find(productname) != -1:
        print "deleting %s" % x
        del adapters[0][x]

    sm.utilities._adapters = adapters

    subscribers = sm.utilities._subscribers
    for x in subscribers[0].keys():
        if x.__module__.find(productname) != -1:
        print "deleting %s" % x
        del subscribers[0][x]

    sm.utilities._subscribers = subscribers

    provided = sm.utilities._provided
    for x in provided.keys():
        if x.__module__.find(productname) != -1:
        print "deleting %s" % x
        del provided[x]


    sm.utilities._provided = provided
