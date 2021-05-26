# import sys
# print(sys.version)

ok_result = ['to','be','or','not','to','be','that','is','the','question']

initial = [ 'not','to','be', 'is','that','the','question']

# add missing
result=['to','be','or']
result.extend(initial)
# miss.reverse()
# for m in miss:
#   result.insert(0,m)

# flip 6,7
flip=result[6]
result[6]=result[7]
result[7]=flip

# Print shit
print(result)
