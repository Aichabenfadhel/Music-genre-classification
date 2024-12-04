import { Component } from '@angular/core';
import { AudioService } from '../audio.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-file-upload',
  standalone: true,
  imports: [FormsModule,CommonModule,RouterLink],
  templateUrl: './file-upload.component.html',
  styleUrl: './file-upload.component.css'
})
export class FileUploadComponent {
  selectedFile: File | null = null;
  predictedGenre: string = 'no predicted genre till now';

  constructor(private audioService: AudioService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
    if (this.selectedFile) {
      this.audioService.uploadAudio(this.selectedFile).subscribe({
        next: (response) => {
          console.log(response);
          this.predictedGenre = response.genre; // Assuming `response.genre` holds the predicted genre
        },
        error: (error) => {
          console.error('Error:', error);
        },
      });
    } else {
      console.warn('No file selected for upload.');
    }
  }
  
}
