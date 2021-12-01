import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Slowdive")
artist_repository.save(artist_1)
artist_2 = Artist("Deftones")
artist_repository.save(artist_2)

album = Album("Souvlaki", "shoegaze", artist_1)
album_repository.save(album)

artist_repository.select_all()

pdb.set_trace()
