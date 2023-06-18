// Import necessary modules and methods
import { LightningElement, wire, track } from 'lwc';
import getCases from '@salesforce/apex/CaseController.getCases'; // Import Apex method to get cases
import closeCases from '@salesforce/apex/CaseController.closeCases'; // Import Apex method to close cases
import { refreshApex } from '@salesforce/apex'; // Import refreshApex function

// Define the component
export default class CaseManager extends LightningElement {
    @track cases = []; // Track cases array to render in datatable
    @track columns = [ // Define the columns for the datatable
        { label: 'Case Number', fieldName: 'CaseNumber' },
        { label: 'Subject', fieldName: 'Subject' },
        { label: 'Status', fieldName: 'Status' },
    ];
    @track selectedCases = []; // Track selected cases array
    wiredCasesResult; // Store the original wired service provisioned value

    @wire(getCases) // Wire an Apex method to a property
    wiredCases(value) { 
        this.wiredCasesResult = value; // Store the original wired service provisioned value
        const { data, error } = value; // Destructure data and error from the provisioned value
        if (data) {
            this.cases = data; // Assign data to cases array if data is present
        } else if (error) {
            console.error('Error retrieving cases', error); // Log error if error is present
        }
    }

    handleRowSelection(event) {
        this.selectedCases = event.detail.selectedRows; // Handle row selection in datatable
    }

    get isButtonDisabled() {
        return this.selectedCases.length === 0; // Disable "Close Cases" button if no cases are selected
    }

    handleCloseCases() {
        const caseIds = this.selectedCases.map(c => c.Id); // Get the IDs of the selected cases
        closeCases({ caseIds }) // Call the Apex method to close cases
            .then(() => {
                // Refresh the cases in the datatable after closing cases
                return refreshApex(this.wiredCasesResult);
            })
            .then(() => {
                // Clear the selected cases array after closing cases
                this.selectedCases = [];
            })
            .catch(error => {
                console.error('Error closing cases', error); // Log error if error occurs when closing cases
            });
    }

    handleRefreshCases() {
        return refreshApex(this.wiredCasesResult); // Refresh the cases in the datatable when "Refresh Cases" button is clicked
    }
}
