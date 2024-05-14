// LC Contest  -> Minimum Substring Partition of Equal Character Frequency
import java.util.*;
class Main{
    static int dfs(int index,String s,HashMap<Integer,Integer>dp){
        if(index==s.length()){
            return 0;
        }
        if(dp.get(index)!=null){
            return dp.get(index);
        }
        HashMap<Character,Integer>hash = new HashMap<Character,Integer>();
        int res = Integer.MAX_VALUE;
        for(int i=index;i<s.length();i++){
            if (hash.get(s.charAt(i))!=null){
                hash.put(s.charAt(i),hash.get(s.charAt(i))+1);
            }
            else{
                hash.put(s.charAt(i),1);
            }
            int flag = 1;
            int prev = -1;
            for(char c : hash.keySet()){
                if(prev==-1){
                    prev = hash.get(c);
                    continue;
                }
                if( hash.get(c)!=prev){
                        flag = 0;
                        break;
                }
            }
            if(flag==1){
                res = Math.min(res,1+dfs(i+1,s,dp));
            }

        }
        dp.put(index,res);
        return res;
    }
    static int minimumSubstringsInPartition(String s){
        HashMap<Integer,Integer>hash = new HashMap<Integer,Integer>();
        return dfs(0,s,hash);
    }
    public static void main(String[] args){
        System.out.println(minimumSubstringsInPartition("fabccddg"));
    }
}