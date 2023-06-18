<template>
    <div class="slds-text-align_left">
        <!-- "Close Cases" button -->
        <lightning-button
            label="Close Cases"
            onclick={handleCloseCases} <!-- Call handleCloseCases method when button is clicked -->
            disabled={isButtonDisabled}> <!-- Disable button if no cases are selected -->
        </lightning-button>
        <!-- "Refresh Cases" button -->
        <lightning-button
            label="Refresh Cases"
            onclick={handleRefreshCases} <!-- Call handleRefreshCases method when button is clicked -->
            class="slds-m-left_small"> <!-- Add margin to the left of the button -->
        </lightning-button>
    </div>
    <!-- Datatable -->
    <lightning-datatable
        key-field="Id" <!-- Set the key field to "Id" -->
        data={cases} <!-- Bind the cases array to the data attribute -->
        columns={columns} <!-- Bind the columns array to the columns attribute -->
        onrowselection={handleRowSelection}> <!-- Call handleRowSelection method when rows are selected -->
    </lightning-datatable>
</template>



