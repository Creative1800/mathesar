import '@testing-library/jest-dom';
import { cellStyle } from '../display';
import type { ColumnPlacement } from '../display';
import type { FilterEntry } from '../filtering';
import { makeApiFilterCondition } from '../filtering';

const placement: ColumnPlacement = {
  width: 25,
  left: 35,
};

let filterEntry: FilterEntry = {
  columnId: 5,
  conditionId: 'conditionId',
  value: undefined,
};

test('cellStyle return expected value', () => {
  expect(cellStyle(placement, 55)).toBe(`width: 25px; left: 90px;`);
});

test('makeApiFilterCondition return correct value if filterEntry is undefined', () => {
  filterEntry = {
    ...filterEntry,
    value: undefined,
  };
  expect(makeApiFilterCondition(filterEntry)).toStrictEqual({
    [filterEntry.conditionId]: [{ column_id: [5] }],
  });
});

test('makeApiFilterCondition return correct value if filterEntry is not undefined', () => {
  filterEntry = {
    ...filterEntry,
    value: 'value',
  };
  expect(makeApiFilterCondition(filterEntry)).toStrictEqual({
    [filterEntry.conditionId]: [{ column_id: [5] }, { literal: ['value'] }],
  });
});
