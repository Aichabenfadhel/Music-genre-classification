import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VggComponent } from './vgg.component';

describe('VggComponent', () => {
  let component: VggComponent;
  let fixture: ComponentFixture<VggComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VggComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VggComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
