// src/app/services/vgg.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class VggService {
  private apiUrl = 'http://localhost:5000/vgg/predict';  

  constructor(private http: HttpClient) {}

  convertAudioToSpectrogram(file: File): Promise<Blob> {
    return new Promise((resolve, reject) => {
      
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      if (!ctx) {
        reject('Failed to get canvas context');
        return; 
      }
  
      canvas.width = 224;
      canvas.height = 224;

      // Simulating spectrogram creation (you would actually process the audio here)
      ctx.fillStyle = 'blue';
      ctx.fillRect(0, 0, 224, 224);

      // Convert the canvas to an image Blob
      canvas.toBlob((blob) => {
        if (blob) {
          resolve(blob);
        } else {
          reject('Failed to create image blob');
        }
      });
    });
  }

  // Upload the spectrogram image to the Flask backend API
  uploadSpectrogram(imageBlob: Blob): Observable<any> {
    const formData = new FormData();
    formData.append('file', imageBlob, 'spectrogram.png');
    return this.http.post<any>(this.apiUrl, formData);
  }

  // Combine audio to spectrogram conversion and API upload
  processAudioAndGetPrediction(file: File): Observable<any> {
    return new Observable((observer) => {
      this.convertAudioToSpectrogram(file)
        .then((spectrogramBlob) => {
          this.uploadSpectrogram(spectrogramBlob).subscribe(
            (response) => {
              observer.next(response);
              observer.complete();
            },
            (error) => {
              observer.error(error);
            }
          );
        })
        .catch((error) => {
          observer.error(error);
        });
    });
  }
}
