#include<iostream.h>
using namespace std;

int main() {
    // Predefined values
    double itemPrice = 10.00;              // Price per item
    int numberOfItems = 5;                 // Number of items
    double taxRate = 8.0;                  // Tax rate as percentage
    double discountPercentage = 10.0;      // Discount rate as percentage

    // Calculations
    double subtotal = itemPrice * numberOfItems;                 // Total before tax and discount
    double taxAmount = subtotal * (taxRate / 100);               // Tax amount
    double discountAmount = subtotal * (discountPercentage / 100);  // Discount amount
    double totalCost = (subtotal + taxAmount) - discountAmount;   // Total cost after applying tax and discount

    // Display results
    cout << "Subtotal: $" << subtotal << endl;
    cout << "Tax Amount: $" << taxAmount << endl;
    cout << "Discount Amount: $" << discountAmount << endl;
    cout << "Total Cost: $" << totalCost << endl;

    return 0;
}
