from math import sqrt
import heapq
class Astar:
    def __init__(self):
        self.map=[]
        self.parent={}
        self.g={}
        self.f={}


    def read_map(self,filename:str):
        with open(filename,'r') as file:
            lines=file.readlines()
            for line in lines:
                line=line.strip()
                line=list(line)
                self.map.append(line)

    def print_ans(self):
        for it in self.map:
            s=''
            print(s.join(it))

    def h(self,node:tuple[int,int],end:tuple[int,int])->int:#这个地方是一个启发项，代表的是当前这个点到终点之间的一个距离
        return abs(node[0]-end[0])+abs(node[1]-end[1])

    def reconstruct_path(self,start,end):
        node=end
        while node != start:
            self.map[node[0]][node[1]]='#'
            node=self.parent[node]
        # self.map[start[0]][start[1]]='*'
        # self.print_ans()

    def A_star(self,start:tuple[int,int],end:tuple[int,int]):
        m=len(self.map)
        n=len(self.map[0])
        dx=[0,1,1,1,0,-1,-1,-1]
        dy=[1,1,0,-1,-1,-1,0,1]
        #init the openlist and the closelist
        openlist=[]
        # 需要注意的一个地方是，这个closelist表示的是还未探索的节点，所以一开始的时候里面应该是空的
        closelist=set()
        self.g[start]=0
        self.f[start]=self.h(start,end)
        heapq.heappush(openlist,(self.f[start],start))
    
        for i in range(8):
            nx,ny=start[0]+dx[i],start[1]+dy[i]
            if 0<=nx and nx<m and ny>=0 and ny<n and self.map[nx][ny]!='*':
                self.parent[(nx,ny)]=start
                self.g[(nx,ny)]=sqrt((start[0]-nx)**2+(start[1]-ny)**2)
                self.f[(nx,ny)]=self.g[(nx,ny)]+self.h(start,end)
                heapq.heappush(openlist,(self.f[(nx,ny)],(nx,ny)))
        
        while openlist:
            _,cur_node=heapq.heappop(openlist)
            closelist.add(cur_node)
            if cur_node==end:
                self.reconstruct_path(start,end)
                return
            for i in range(8):
                nx,ny=cur_node[0]+dx[i],cur_node[1]+dy[i]
                if 0<=nx and nx<m and ny>=0 and ny<n and self.map[nx][ny]!='*'\
                and (nx,ny) not in closelist:
                    g=self.g[(cur_node)]+sqrt((cur_node[0]-nx)**2+(cur_node[1]-ny)**2)
                    '''这里有一个巧妙的技巧，由于openlist，不是一个集合或者字典，所以不能够查询
                       所以这里使用的是self.g这个字典
                    '''
                    if (nx,ny) not in self.g or g<self.g[(nx,ny)]:
                        # update the member variable
                        self.g[(nx,ny)]=g
                        self.f[(nx,ny)]=g+self.h((nx,ny),end)
                        self.parent[(nx,ny)]=cur_node
                        heapq.heappush(openlist,(self.f[(nx,ny)],(nx,ny)))
        print('No resolution')
        return
                    

 

def main():
    astar = Astar()
    astar.read_map("map.txt")
    print("Initial map:")
    astar.print_ans()
    start = (1, 1)  # 假设起点是 (1, 1)，这应该对应地图中的 'S'
    end = (13, 8)    # 假设终点是 (4, 3)，这应该对应地图中的 'E'
    astar.A_star(start, end)
    print("\nPath from start to end:")
    astar.print_ans()

if __name__ == "__main__":
    main()