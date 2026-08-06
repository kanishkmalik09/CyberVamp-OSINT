#!/usr/bin/env python3
"""
HadesIntel - Phone OSINT Dashboard
Phone number validation via NumVerify API
"""

import os
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ============================================================
# CONFIGURATION – SET YOUR API KEY HERE OR AS ENV VAR
# ============================================================

# Option 1: Set as environment variable (recommended)
# In terminal: set NUMVERIFY_KEY=your_key_here
NUMVERIFY_KEY = os.environ.get('NUMVERIFY_KEY', '')

# Option 2: Or paste your key directly here (for testing only)
# NUMVERIFY_KEY = 'your_numverify_key_here'

# ============================================================
# PHONE OSINT (NumVerify)
# ============================================================

def osint_phone(phone):
    """
    Query NumVerify API for phone number validation and carrier info.
    Returns validity, carrier, location, and line type.
    """
    results = {
        'input': phone,
        'service': 'NumVerify',
        'status': 'error',
        'data': None,
        'error': None
    }

    if not NUMVERIFY_KEY:
        results['error'] = 'NumVerify API key not configured. Set NUMVERIFY_KEY.'
        return results

    # Clean phone number (remove spaces, dashes, plus, etc.)
    phone_clean = ''.join(filter(str.isdigit, phone))
    if not phone_clean:
        results['error'] = 'Invalid phone number format. Please enter only digits.'
        return results

    try:
        # Free tier uses HTTP, not HTTPS
        url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_KEY}&number={phone_clean}"
        resp = requests.get(url, timeout=15)

        if not resp.text or resp.text.strip() == '':
            results['error'] = 'Empty response from NumVerify API.'
            return results

        try:
            data = resp.json()
        except json.JSONDecodeError:
            results['error'] = f'Invalid response: {resp.text[:100]}...'
            return results

        # Check for API errors
        if data.get('success') is False:
            error_info = data.get('error', {})
            error_code = error_info.get('code', 'unknown')
            error_msg = error_info.get('info', 'Unknown error')

            if error_code == 101:
                error_msg = 'Invalid API key. Please check NUMVERIFY_KEY.'
            elif error_code == 104:
                error_msg = 'Monthly API limit reached. Please wait or upgrade.'
            elif error_code == 102:
                error_msg = 'Invalid phone number format.'
            elif error_code == 103:
                error_msg = 'API key not activated or out of credits.'

            results['error'] = f'NumVerify Error ({error_code}): {error_msg}'
            return results

        # Extract validation data
        if data.get('valid'):
            results['status'] = 'success'
            results['data'] = {
                'valid': True,
                'country': data.get('country_name', 'N/A'),
                'country_code': data.get('country_code', 'N/A'),
                'carrier': data.get('carrier', 'N/A'),
                'location': data.get('location', 'N/A'),
                'line_type': data.get('line_type', 'N/A'),
                'international_format': data.get('international_format', 'N/A'),
                'local_format': data.get('local_format', 'N/A'),
                'summary': f"Valid {data.get('line_type', '')} number from {data.get('country_name', 'unknown')} via {data.get('carrier', 'unknown carrier')}"
            }
        else:
            results['status'] = 'success'
            results['data'] = {
                'valid': False,
                'summary': 'Invalid or non-existent phone number'
            }

    except requests.exceptions.Timeout:
        results['error'] = 'NumVerify API timeout. Please try again.'
    except requests.exceptions.ConnectionError:
        results['error'] = 'Cannot connect to NumVerify API. Check internet.'
    except Exception as e:
        results['error'] = f'Unexpected error: {str(e)}'

    return results


# ============================================================
# FLASK ROUTES
# ============================================================

@app.route('/')
def index():
    """Serve the frontend"""
    return render_template('index.html')


@app.route('/api/osint', methods=['POST'])
def osint_search():
    """API endpoint for phone OSINT searches."""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    search_type = data.get('type', '').lower()
    search_value = data.get('value', '').strip()

    if not search_value:
        return jsonify({'error': 'No search value provided'}), 400

    if search_type != 'phone':
        return jsonify({'error': 'Only "phone" searches are supported.'}), 400

    result = osint_phone(search_value)
    result['timestamp'] = datetime.now().isoformat()

    return jsonify(result)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'service': 'NumVerify',
        'configured': bool(NUMVERIFY_KEY),
        'timestamp': datetime.now().isoformat()
    })


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    status = '✅ NumVerify configured' if NUMVERIFY_KEY else '❌ Missing (set NUMVERIFY_KEY)'
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║  HadesIntel - Phone OSINT Dashboard                      ║
    ║  Service: NumVerify                                     ║
    ║                                                          ║
    ║  Status: %s
    ║                                                          ║
    ║  Open: http://127.0.0.1:5000                            ║
    ╚═══════════════════════════════════════════════════════════╝
    """ % status)

    app.run(debug=True, host='0.0.0.0', port=5000)