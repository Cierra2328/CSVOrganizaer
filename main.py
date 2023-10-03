from process import Process_file

def main():
    #get file from user
    inputFile = input("Enter the name of a file for processing: ")

    #open user's file and output file that will be written to
    inFile = open(inputFile, 'r')
    outFile = open("ProjectDataSet-500Output.txt", 'w')

    #keep count of how many records are being processed
    count = 0

    #For each line in the file
    for line in inFile:
        count = count + 1   #we are going to keep a count of the amount of records being processed
        processed = Process_file(line) #we call the class and give it the line of text, this will return an object called 'processed'
        state = processed.state(processed.compAddressSt) #this calls the 'state' function within the Procee_file class
        if processed.bool == 1: #get info from class 
            processed.limit = str(processed.limit) + 'M '  #and change the letter depending on the limits
        else:
            processed.limit = str(processed.limit) + 'K '
        #this is a line of data that will be written to the output file
        output =  ('' + processed.name + processed.contactLastName + processed.contactFirstName +
                  processed.compStreetAddress + processed.compAddressCity + ' ' + state + ' ' +
                  processed.compAddressZip + ' ' + processed.compContact + ' ' + processed.altContact + ' ' + processed.alphaKey + ' ' +
                  processed.betaKey + ' ' + processed.regions + ' ' + processed.compCode + ' ' + processed.custType + ' ' + processed.limit +
                  processed.ID + '\n\n')
        outFile.write(output) #writing to the file

    outFile.close() #close the file just because
    print(str(count) + ' records with ' + str(count * 16) + ' fields processed') #nice summary for the user
        
        
#gotta run the script
if __name__ == "__main__":
    main()
