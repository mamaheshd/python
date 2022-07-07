import psycopg2
mydb=psycopg2.connect(
    database="mahesh dahal",
    user="postgres",
    password="maipokhari1",
    host="localhost",
    port=5432,
)
cursor=mydb.cursor()
query='select * from "student"'
cursor.execute(query)
array=list(cursor.fetchall())

def mergeSort(array):
    if len(array) > 1:
        m = len(array)//2
        L = array[:m]
        r = array[m:]

        mergeSort(L)
        mergeSort(r)

        i = j = k = 0
        while i < len(L) and j < len(r):
            if L[i][2] < r[j][2]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)