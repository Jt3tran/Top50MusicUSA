fetch('spotify_top50_with_art.csv')
    .then(response => response.text())
    .then(data => {
        const rows = data.split('\n').slice(1); // Skip Header
        const container = document.querySelector('.track-list'); // use your new div
        container.innerHTML = '';

        rows.slice(0, 50).forEach(row => {  // show first 10 items
            if (row.trim() == '') return;
            const [position, track, artist, albumArt] = row.split(',');

            const trackItem = document.createElement('div');
            trackItem.className = 'track-item';

            const number = document.createElement('span');
            number.className = 'track-number';
            number.textContent = position;

            const img = document.createElement('img');
            img.className = 'album-art';
            img.src = albumArt ? albumArt : 'https://i.scdn.co/image/ab67616d0000b273e67611dbbf69a90d0b6cb738';
            img.alt = 'Album Art';

            const info = document.createElement('div');
            info.className = 'track-info';

            const title = document.createElement('div');
            title.className = 'track-title';
            title.textContent = track;

            const artistName = document.createElement('div');
            artistName.className = 'track-artist';
            artistName.textContent = artist;

            info.appendChild(title);
            info.appendChild(artistName);

            trackItem.appendChild(number);
            trackItem.appendChild(img);
            trackItem.appendChild(info);

            container.appendChild(trackItem);
        });
    });
