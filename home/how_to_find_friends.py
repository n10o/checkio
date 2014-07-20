# encoding: utf-8
def check_connection(network, first, second):
    # construct network
    friends = []
    for nw in network:
        nwlist = nw.split("-")
        friends.append(nwlist)
    # e.x. friends == [['dr101', 'mr99'], ['mr99', 'out00']]

    bonds = []
    for friend in friends:
        detectbonds = False
        i = 0
        for bond in bonds:
            if friend[0] in bond:
                bonds[i].append(friend[1])
                detectbonds = True
            elif friend[1] in bond:
                bonds[i].append(friend[0])
                detectbonds = True
            i += 1

        # firstloopと該当するbondsがなかった場合に新しい友だちリストを加える
        if detectbonds == False:
            bonds.append(friend)

        #TODO bondsを全て再確認し、仲間がいたらリストを結合する
        # 非効率なので、ロジック再考
        #for bond in bonds:
            


    print bonds

    for bond in bonds:
        if first in bond:
            if second in bond:
                return True

    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
