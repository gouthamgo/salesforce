public with sharing class CaseController {
    // Method to get all Cases
    @AuraEnabled(cacheable=true)
    public static List<Case> getCases() {
        return [SELECT Id, CaseNumber, Subject, Status FROM Case WHERE Status != 'Closed'];
    }

    // Method to close Cases in bulk
    @AuraEnabled
    public static void closeCases(List<Id> caseIds) {
        List<Case> casesToClose = [SELECT Id, Status FROM Case WHERE Id IN :caseIds];
        for(Case c : casesToClose) {
            c.Status = 'Closed';
        }
        update casesToClose;
    }
}
