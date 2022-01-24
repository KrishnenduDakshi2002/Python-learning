SELECT Track.Track_name,Genre.Genre_name,Album.Album_name,Artist.Artist_name FROM Track JOIN Genre JOIN Album JOIN Artist ON
Track.Album_id == Album.id AND Track.Genre_id == Genre.id AND Album.id == Artist.id

