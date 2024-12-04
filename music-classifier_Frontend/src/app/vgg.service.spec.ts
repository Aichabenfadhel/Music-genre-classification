import { TestBed } from '@angular/core/testing';

import { VggService } from './vgg.service';

describe('VggService', () => {
  let service: VggService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VggService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
