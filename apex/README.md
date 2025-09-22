--> core idea SF is multi tenant
    --> Resource limits (Governor Limits)
    --> Bulk processing requried 
    --> Context Awareness
--> SOQAL --> 100 queries max


example :

#bad version is 

for(Account acc: accounts){
    Contact con = [SELECT Id FROM Contact WHERE AccountId = acc.Id];
}

Map<Id, Contact> contactsByAccountId = new Map<Id,Contact>();
for(Contact con: [SELECT Id, Account FROM Contact WHERE AccountId IN :accountIds]){
    contactsByAccountId.put(con.AccountId,con);
}
<!-- 0(1) lookups with map -->