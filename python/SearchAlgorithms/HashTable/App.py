from HashTable import HashTable

newHashTable = HashTable(10)

newHashTable.insert(78, 'Dovah')
newHashTable.insert(8, 'Geralt')
newHashTable.insert(9, 'Snake')
newHashTable.insert(91, 'Quiet')
newHashTable.insert(8, 'Viper')

print(newHashTable.get(8))
