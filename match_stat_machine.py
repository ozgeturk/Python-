baseball_stats = [['Martin,Leonys', 'TEX', 147, 457, 66, 119, 21, 6, 8], ['Smoak,Justin', 'SEA', 131, 454, 53, 108, 19, 0, 20], ['Ibanez,Raul', 'SEA', 124, 454, 54, 110, 20, 2, 29], ['Infante,Omar', 'DET', 118, 453, 54, 144, 24, 3, 10], ['Bautista,Jose', 'TOR', 118, 452, 82, 117, 24, 0, 28], ['Blanco,Gregor', 'SF', 141, 452, 50, 120, 17, 6, 3], ['Rosario,Wilin', 'COL', 121, 449, 63, 131, 22, 1, 21], ['Uggla,Dan', 'ATL', 136, 448, 60, 80, 10, 3, 22],
                  ['Moss,Brandon', 'OAK', 145, 446, 73, 114, 23, 3, 30], ['Tulowitzki,Troy', 'COL', 126, 446, 72, 139, 27, 0, 25], ['Mauer,Joe', 'MIN', 113, 445, 62, 144, 35, 0, 11], ['Overbay,Lyle', 'NYY', 142, 445, 43, 107, 24, 1, 14], ['Pollock,A.J.', 'ARI', 137, 443, 64, 119, 28, 5, 8], ['Drew,Stephen', 'BOS', 124, 442, 57, 112, 29, 8, 13], ['Viciedo,Dayan', 'CWS', 124, 441, 43, 117, 23, 3, 14], ['Dirks,Andy', 'DET', 131, 438, 60, 112, 16, 2, 9],
                  ['Martin,Russell', 'PIT', 127, 438, 51, 99, 21, 0, 15], ['Shuck,J.B.', 'LAA', 129, 437, 60, 128, 20, 3, 2], ['Murphy,David', 'TEX', 142, 436, 51, 96, 26, 1, 13], ['Crawford,Carl', 'LAD', 116, 435, 62, 123, 30, 3, 6], ['Castro,Jason', 'HOU', 120, 435, 63, 120, 35, 1, 18], ['Ellis,Mark', 'LAD', 126, 433, 46, 117, 13, 2, 6], ['Rios,Alex', 'CWS', 109, 430, 57, 119, 22, 2, 12], ['Wright,David', 'NYM', 112, 430, 63, 132, 23, 6, 18],
                  ['Stubbs,Drew', 'CLE', 146, 430, 59, 100, 21, 2, 10], ['Saltalamacchia,Jarrod', 'BOS', 121, 425, 68, 116, 40, 0, 14], ['Byrd,Marlon', 'NYM', 117, 425, 61, 121, 26, 5, 21], ['Stanton,Giancarlo', 'MIA', 116, 425, 62, 106, 26, 0, 24], ['Harper,Bryce', 'WAS', 118, 424, 71, 116, 24, 3, 20], ['Wells,Vernon', 'NYY', 130, 424, 45, 99, 16, 0, 11], ['Ruggiano,Justin', 'MIA', 128, 424, 49, 94, 18, 1, 18], ['Keppinger,Jeff', 'CWS', 117, 423, 38, 107, 13, 1, 4],
                  ['Rasmus,Colby', 'TOR', 118, 417, 57, 115, 26, 1, 22], ['Fowler,Dexter', 'COL', 119, 415, 71, 109, 18, 3, 12], ['Joyce,Matt', 'TB', 140, 413, 61, 97, 22, 0, 18], ['Cruz,Nelson', 'TEX', 109, 413, 49, 110, 18, 0, 27], ['Montero,Miguel', 'ARI', 116, 413, 44, 95, 14, 0, 11], ['Kozma,Pete', 'STL', 143, 410, 44, 89, 20, 0, 1], ['Peralta,Jhonny', 'DET', 107, 409, 50, 124, 30, 0, 11], ['Barnes,Brandon', 'HOU', 136, 408, 46, 98, 17, 1, 8],
                  ['Gillaspie,Conor', 'CWS', 134, 408, 46, 100, 14, 3, 13], ['Saunders,Michael', 'SEA', 132, 406, 59, 96, 23, 3, 12], ['LeMahieu,DJ', 'COL', 109, 404, 39, 113, 21, 3, 2], ['Florimon,Pedro', 'MIN', 134, 403, 44, 89, 17, 0, 9], ['Jones,Garrett', 'PIT', 144, 403, 41, 94, 26, 2, 15], ['Lawrie,Brett', 'TOR', 107, 401, 41, 102, 18, 3, 11], ['Cain,Lorenzo', 'KC', 115, 399, 54, 100, 21, 3, 4], ['Helton,Todd', 'COL', 124, 397, 41, 99, 22, 1, 15],
                  ['Lagares,Juan', 'NYM', 121, 392, 35, 95, 21, 5, 4], ['Pujols,Albert', 'LAA', 99, 391, 49, 101, 19, 0, 17]]

command, name = input().split()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def baseball_stat_machine(command, name):
    team_player = 0
    list_of_tuples = []
    if command == "BATTING":
        for i in baseball_stats:
            if i[0] == name:
                hits = i[5]
                at_bats = i[3]
                batting_avg = hits / at_bats
                return batting_avg
    elif command == "SLUGGING":
        for i in baseball_stats:
            if i[0] == name:
                singles = i[5] - (i[6] + i[7] + i[8])
                total_bases = singles + 2*i[6] + 3*i[7] + 4*i[8]
                slugging_perc = total_bases / i[3]
                return slugging_perc
    elif command == "TEAM":
        for i in baseball_stats:
            if i[1] == name:
                team_player += 1
        return team_player
    elif command == "HOMERUN":
        for i in baseball_stats:
            if i[1] == name:
                tuple = (i[0], i[8])
                list_of_tuples.append(tuple)
        list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1])

        return list_of_tuples

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

result = baseball_stat_machine(command, name)

if type(result) == int:
    print(result)
elif type(result) == float:
    print("%.2f" % result)
else:
    for player in result:
        print(player, end=" ")
