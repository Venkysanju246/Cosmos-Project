// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { PdfChatComponent } from './pdf-chat/pdf-chat.component';

@NgModule({
  declarations: [
    AppComponent,
    PdfChatComponent,
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
