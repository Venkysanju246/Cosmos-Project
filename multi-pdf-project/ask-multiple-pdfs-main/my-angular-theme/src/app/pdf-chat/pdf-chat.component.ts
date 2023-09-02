import { Component } from '@angular/core';

@Component({
  selector: 'app-pdf-chat',
  templateUrl: './pdf-chat.component.html',
  styleUrls: ['./pdf-chat.component.css']
})
export class PdfChatComponent {
  // Define a method to handle the "Get Started" button click
  onGetStartedButtonClick() {
    // Add your functionality here
    alert('Button Clicked!'); 
    window.location.href = "http://localhost:8501/";
    
  }
}
