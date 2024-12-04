// src/app/vgg/vgg.component.ts
import { Component } from '@angular/core';
import { VggService } from '../vgg.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-vgg',
  standalone:true,
  imports: [FormsModule,CommonModule,RouterLink],
  templateUrl: './vgg.component.html',
  styleUrls: ['./vgg.component.css'],
})
export class VggComponent {
  selectedFile: File | null = null;
  predictionResult: any = null;
  loading: boolean = false;
  errorMessage: string | null = null;

  constructor(private vggService: VggService) {}

  onFileChange(event: any): void {
    this.selectedFile = event.target.files[0];
    this.errorMessage = null;  // Reset error message when a new file is selected
  }

  onSubmit(): void {
    if (this.selectedFile) {
      this.loading = true;
      console.log('selected file',this.selectedFile);
      
      this.vggService.processAudioAndGetPrediction(this.selectedFile).subscribe(
        (response) => {
          console.log(response);
          
          this.loading = false;
          this.predictionResult = response.predictions;
        },
        (error) => {
          this.loading = false;
          this.errorMessage = 'Failed to process the file. Please try again.';
        }
      );
    } else {
      this.errorMessage = 'Please select an audio file.';
    }
  }
}
