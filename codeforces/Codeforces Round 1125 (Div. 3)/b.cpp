#include<bits/stdc++.h>
using namespace std ;

int main (){
   int t  ;
   cin>>t  ;
    while(t--){

        int n ;
        cin>>n ;
        string s;
        cin>>s ;

        stack<int> st ;
        bool printed [100000]={false} ;

        for(int i=0 ; i<n ; i++){
            int doc=i+1 ;
            if(s[i]=='1'){
                st.push(doc);
            }

            else if(s[i]=='2'){
            if(!st.empty()){
                printed[st.top()]=true;
                st.pop();
            }
            else{
                printed[doc]=true ;
            }
        }
        else if(s[i]=='3'){
            printed[doc]=true;
        }

    }

    int not_print_count=0 ;

    for(int i=1 ; i<=n ; i++){
        if(!printed[i]){
            not_print_count++ ;
        }
    }

    cout<<not_print_count <<'\n' ;

    for(int i=1 ; i<=n ; i++){
        if(!printed[i]){
            cout<<i<< " " ;
        }
    }
     cout<<'\n';

    }



return 0 ;
}
