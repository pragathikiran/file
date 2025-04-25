file_read = open('file.text','r')
print("file in read mode -")
print(file_read.read())
file_read.close()

file_write = open("file.text","w")

file_write.write("File in write mode ....")
file_write.write("POINTS ON HARRY POTTER")
file_write.close()

file_append = open("file.text","a")

file_append.write("\n file in append mode .....")
file_append.write("I LIKE HARRY POTTER")
file_append.close()