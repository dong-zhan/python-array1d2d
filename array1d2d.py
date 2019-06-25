class array1D:

    def __init__(self, count):

        self.arr = [None] * count

    def __getitem__(self, x):

        return self.arr[x]

    def __setitem__(self, x, data):

        self.arr[x] = data

        

class array2D:

    def __init__(self, x, y):

        #self.arr = [array1D(column)] * row   #WRONG, why??, looks like only one instance has been created, all other entries are referencing this instance.

        self.arr = [array1D(x) for i in range(y)]  

    #def __getitem__(self, x):

    #    return self.arr[x]

    def get(self, x, y):

        return self.arr[y][x]

    def set(self, x, y, data):

        self.arr[y][x] = data

    def dump(self):

        for row in self.arr:

            print(row.arr)



class grid2D(array2D):

    def __init__(self, cellSizeX, cellSizeY, gridX, gridY, origX, origY):

        super(grid2D, self).__init__(gridX, gridY)

        self.cellSizeX = cellSizeX

        self.cellSizeY = cellSizeY

        self.invCellSizeX = 1/cellSizeX

        self.invCellSizeY = 1/cellSizeY

        self.gridX = gridX      #number of grid lines in x

        self.gridY = gridY      #number of grid lines in y   

        self.origX = origX      #real world grid coordinates of grid(0,0)

        self.origY = origY      #real world grid coordinates of grid(0,0)

        

        for row in range(gridY):

            for col in range(gridX):

                self.arr[row][col] = {}

            

    def worldXY2gridXY(self, x, y):

        return int(x * self.invCellSizeX + self.origX), int(y * self.invCellSizeY + self.origY)

        

    def getCellObjs(self, x, y):

        gx,gy = self.worldXY2gridXY(x,y)

        return self.get(x, y)

        

    def find(self, id, x, y):

        gx,gy = self.worldXY2gridXY(x,y)

        cellObjs = self.get(gx, gy)

        sid = str(id)

        if sid in cellObjs:

            return cellObjs[sid]

        return None

        

    def move(self, id, oldX, oldY, newX, newY):

        gOldX,gOldY = self.worldXY2gridXY(oldX,oldY)

        gNewX,gNewY = self.worldXY2gridXY(newX,newY)

        if gOldX == gNewX and gOldY == gNewY:

            return

        sid = str(id)

        oldCellObjs = self.get(gOldX, gOldY)        

        newCellObjs = self.get(gNewX, gNewY)            

        newCellObjs[sid] = oldCellObjs[sid]        

        del oldCellObjs[sid]

        

    

    def delete(self, id, x, y):

        cellObjs = self.getCellObjs(x, y)

        del cellObjs[str(id)]

        return True

        

    def add(self, id, obj, x, y):

        gx,gy = self.worldXY2gridXY(x,y)

        cellObjs = self.get(gx, gy)

        sid = str(id)

        if sid in cellObjs:

            return None

        cellObjs[sid] = obj      

    

    def dump(self):

        c = 0

        for row in self.arr:

            r = 0

            for objs in row:

                print(r,c,objs)

                r = r + 1

            c = c + 1
