// package graphs;

// class DSU{
//     int[] parent;
//     int[] size;
//     DSU(int V){
//         parent = new int[V];
//         for(int i=0;i<V;i++){
//             parent[i] = i;
//         }
//         size = new int[V];
//     }
//     public int findParent(int node){
//         if (node == parent[node]) return node;
//         int p = findParent(parent[node]);
//         return p;
//     }
//     public void findBySize(int u, int v){
//         int u_vertex = findParent(u);
//         int v_vertex = findParent(v);
//         if(size[u_vertex] > size[v_vertex]){
//             size[u_vertex] += size[v_vertex];
//             parent[v_vertex] = u_vertex;
//         }
//         else{
//             size[v_vertex] += size[u_vertex];
//             parent[u_vertex] = v_vertex;
//         }
//     }
// }


// public class maximumEdgerRemove {
//     public static void main(String[] args) {
//             int n  = 4;
//             int [][] edges = {{3,1,2},{3,2,3},{1,1,3},{1,2,4},{1,1,2},{2,3,4}};
//             DSU alice = new DSU(n+1);
//             DSU bob = new DSU(n+1);
//     }
// }
