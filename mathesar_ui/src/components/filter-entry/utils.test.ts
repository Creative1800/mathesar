import '@testing-library/jest-dom';
import { validateFilterEntry } from './utils';

describe('utils tests', () => {
  test('value is empty', () => {
    expect(
      validateFilterEntry({ id: 'id', name: 'name', parameters: [] }, ''),
    ).toBeFalsy();
  });
});
