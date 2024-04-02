#include <bits/stdc++.h>
#include <vector>
using namespace std;
const int N=6e6+11;
int n,m;
int fa[N],sz[N];
int find(int x){
    if(fa[x]!=x)fa[x]=find(fa[x]);
    return fa[x];
}
bool is_united(int u,int v){
    return find(u)==find(v);
}
bool unite(int f,int t){
    f=find(f),t=find(t);
    if(f!=t){
        fa[f]=t;
        sz[t]+=sz[f];
        return true;
    }
    return false;
}
vector<pair<int,int>> allEdges;
int main(){
    scanf("%d",&n);
    for(int i=0;i<n;++i){
        fa[i]=i;
        sz[i]=1;
    }
    int u,v;
    while(scanf("%d%d",&u,&v)!=EOF){
        if(u==v)continue;
        allEdges.emplace_back(u,v);
        unite(u,v);
    }
    int maxSize=0,maxV=-1;
    for(int i=0;i<n;++i){
        if(sz[i]>maxSize){
            maxSize=sz[i];
            maxV=i;
        }
    }
    if(maxSize==n){
        cerr<<"Already Connected"<<endl;
        return 0;
    }
    map<int,int> mp;
    int mpTail=0;
    printf("%d\n",maxSize);
    vector<pair<int,int> >newEdges;
    for(auto e:allEdges){
        if(find(e.first)==maxV){
            if(mp.count(e.first)==0){
                mp.insert(make_pair(e.first,mpTail++));
            }
            if(mp.count(e.second)==0){
                mp.insert(make_pair(e.second,mpTail++));
            }
            int u=mp.at(e.first),v=mp.at(e.second);
            newEdges.emplace_back(min(u,v),max(u,v));
        }

    }
    sort(newEdges.begin(),newEdges.end());
    for(auto e:newEdges){
        printf("%d %d\n",e.first,e.second);
    }
    return 0;
}
