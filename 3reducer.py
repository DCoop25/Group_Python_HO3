input_file = open("02.txt","r")
output_file = open("r.txt", "w")

currentKey = ""
currentMax = 0.0

for line in input_file:
  data = line.strip().split('\t')
  category, amount = data

  if category != currentKey:
    if currentKey:
      # output the last key value pair result
      output_file.write(currentKey + '\t' + str(currentMax)+'\n')

    # start over when changing keys
    currentKey = category 
    currentMax = 0.0
  
  # apply the aggregation function
  if (currentMax < float(amount)):
    currentMax = float(amount)

# output the final entry when done
output_file.write(currentKey + '\t' + str(currentMax)+'\n')

input_file.close()
output_file.close()
print("Done")