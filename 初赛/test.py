# #include <cstdio>
# #include <iostream>
# using namespace std;
#
# const int maxn = 1e6+7;
#
# int n,head[maxn],cnt,color[maxn],sonNumber[maxn];//sonNumber表示子树大小
# bool isFailed = false;//是否染色失败
#
# struct Edge {
#     int from, to;
# }e[maxn<<1];
#
# inline void add(int u, int v)
# {
#     e[++cnt].from = head[u];
#     e[cnt].to = v;
#     head[u] = cnt;
# }
#
# int calcSon(int nowPoint,int lastPoint)//计算子树大小,lastPoint表示上一个点
# {
#     int sum = 1;
#     for(int i = head[nowPoint];i;i = e[i].from) {
#         int nextPoint = e[i].to;
#         if(nextPoint == lastPoint)
#             continue;
#         sum += calcSon(nextPoint, nowPoint);
#     }
#     return sonNumber[nowPoint] = sum;
# }
#
# void dfs(int nowPoint, int lastPoint, int nowColor)//用0,1表示点的颜色
# {
#     if(isFailed)
#         return ;
#     color[nowPoint] = nowColor;
#     int cnt = 0 ;
#     for(int i = head[nowPoint]; i; i = e[i].from) {
#         int nextPoint = e[i].to;
#         if(nextPoint != lastPoint)
#             cnt += sonNumber[nextPoint] & 1;//判断它的子节点的树大小是否有且只有一个奇数
#     }
#     if(color[nowPoint] == color[lastPoint]) {//情况一
#         if(cnt) {
#             isFailed = true;
#             return ;
#         }
#         for(int i = head[nowPoint]; i; i = e[i].from) {
#             int nextPoint = e[i].to;
#             if(nextPoint != lastPoint)
#                 dfs(nextPoint, nowPoint, nowColor^1);
#         }
#     }
#     else {//情况二
#         if(cnt != 1) {
#             isFailed = true;
#             return ;
#         }
#         for(int i = head[nowPoint]; i ;i = e[i].from) {
#             int nextPoint = e[i].to;
#             if(nextPoint != lastPoint) {
#                 if(sonNumber[nextPoint] & 1)//如果是大小为奇数的子树
#                     dfs(nextPoint, nowPoint, nowColor);
#                 else
#                     dfs(nextPoint, nowPoint,  nowColor^1);
#             }
#         }
#     }
# }
#
# int main()
# {
#     scanf("%d", &n);
#     for(int i = 1; i < n; ++i) {
#         int x, y;
#         scanf("%d%d", &x, &y);
#         add(x,y); add(y,x);
#     }
#     sonNumber[1] = calcSon(1, 0);
#     dfs(1,0,1);
#     if(isFailed)
#         printf("-1\n");
#     else {
#         for(int i = 1; i <= n; ++i) {
#             if (color[i])
#                 printf("B");
#             else
#                 printf("R");
#         }
#     }
#     return 0;
# }