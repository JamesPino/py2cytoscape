__author__ = 'kono'


class NetworkUtil(object):

    @staticmethod
    def name2suid(network, obj_type='node'):
        if obj_type is 'node':
            table = network.get_node_table()
        elif obj_type is 'edge':
            table = network.get_edge_table()
        else:
            raise ValueError('No such object type: ' + obj_type)
        name2suid = {}
        for suid, name in table[['SUID', 'name']].values:
            name2suid[name] = suid
        return name2suid

