@isTest
public class CaseControllerTest {
    @isTest static void testGetCases() {
        // Given
        // Insert a test case
        Case c = new Case(Status = 'New', Subject = 'Test Case');
        insert c;
        
        // When
        // Call getCases method
        List<Case> cases = CaseController.getCases();
        
        // Then
        // Check that the case is returned
        System.assertEquals(1, cases.size());
        System.assertEquals(c.Id, cases[0].Id);
    }
    
    @isTest static void testCloseCases() {
        // Given
        // Insert two test cases
        Case c1 = new Case(Status = 'New', Subject = 'Test Case 1');
        Case c2 = new Case(Status = 'New', Subject = 'Test Case 2');
        insert new List<Case>{c1, c2};
        
        // When
        // Call closeCases method
        CaseController.closeCases(new List<Id>{c1.Id, c2.Id});
        
        // Then
        // Check that the cases are closed
        c1 = [SELECT Status FROM Case WHERE Id = :c1.Id];
        c2 = [SELECT Status FROM Case WHERE Id = :c2.Id];
        System.assertEquals('Closed', c1.Status);
        System.assertEquals('Closed', c2.Status);
    }
}