import { render } from '@testing-library/svelte';
import '@testing-library/jest-dom';
import CellBackground from '../RowCellBackgrounds.svelte';

describe('RowCellBackgrounds tests', () => {
  test('CellBackground rendering', () => {
    const { container } = render(CellBackground);

    const cell = container.querySelector('.cell-background');
    expect(cell).toBeInTheDocument();
  });

  test('isSelected is true', () => {
    const { container } = render(CellBackground, {
      props: {
        isSelected: true,
      },
    });

    const cell = container.querySelector('.cell-background');
    expect(cell).toBeInTheDocument();
    expect(cell).toHaveStyle(
      'background-color: var(--cell-bg-color-row-selected)',
    );
  });

  test('bg-color var(processing) if isProcessing is true', () => {
    const { container } = render(CellBackground, {
      props: {
        isProcessing: true,
      },
    });

    const cell = container.querySelector('.cell-background');
    expect(cell).toBeInTheDocument();
    expect(cell).toHaveStyle(
      'background-color: var(--cell-bg-color-processing)',
    );
  });

  test('bg-color var(error) if hasErrors is true', () => {
    const { container } = render(CellBackground, {
      props: {
        hasErrors: true,
      },
    });

    const cell = container.querySelector('.cell-background');
    expect(cell).toBeInTheDocument();
    expect(cell).toHaveStyle('background-color: var(--cell-bg-color-error)');
  });
});
