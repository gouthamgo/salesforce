

List<String> items = new List<String>();
items.add('item1')

Set<String> uitems = new Set<String>();
uitems.add('trail')


Map<String,String> book = new Map<String,String>();
book.put('check','list')


List<String> checking = new List<String>{'Contact1', 'Contact2', 'Contact3'};
List<String> levels = new List<String>{'A','B','A'};

List<String> items = new List<String>{'p1','p2','p1','p2','p1'};
List<String> q = new List<Sting>();


Integer count = 0;

for(String item: items){
    if(item =='p1'){
        count = count + 1;
    }
}


/*
Say we got accounts --> want to find Melbourne

*/

List<Account> allAccounts = [SELECT Name,BillingState FROM Account];
List<Account> melAccounts = new List<Account>();

for(Account acc: allAccounts){
    if(acc.BillingState == 'mel'){
        melAccounts.add(acc)
    }
}

