import { render } from '@testing-library/react'
import SearchMap from '../../components/SearchMap'

describe('SearchMap', () => {
  test('renders SearchMap component without crashing', () => {
    render(<SearchMap />)
  });

  test('renders AnyReactComponent with correct text', () => {
      const { getByText } = render(<SearchMap />);
      const markerText = getByText(/My Marker/i);
      expect(markerText).toBeInTheDocument();
    });

  test('has correct style for the map container', () => {
    const { container } = render(<SearchMap />);
    const mapContainer = container.firstChild;
    
    expect(mapContainer).toHaveStyle('height: 600px');
    expect(mapContainer).toHaveStyle('width: 100%');
  });
});
