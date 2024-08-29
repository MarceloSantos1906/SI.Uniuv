/*
  Warnings:

  - You are about to alter the column `A` on the `_AuthorsToBooks` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.
  - You are about to alter the column `B` on the `_AuthorsToBooks` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.
  - You are about to alter the column `A` on the `_BooksToGenres` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.
  - You are about to alter the column `B` on the `_BooksToGenres` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.
  - The primary key for the `authors` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - You are about to alter the column `authorId` on the `authors` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.
  - The primary key for the `books` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - You are about to alter the column `booksId` on the `books` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.
  - The primary key for the `genres` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - You are about to alter the column `genreId` on the `genres` table. The data in that column could be lost. The data in that column will be cast from `String` to `Int`.

*/
-- RedefineTables
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new__AuthorsToBooks" (
    "A" INTEGER NOT NULL,
    "B" INTEGER NOT NULL,
    CONSTRAINT "_AuthorsToBooks_A_fkey" FOREIGN KEY ("A") REFERENCES "authors" ("authorId") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_AuthorsToBooks_B_fkey" FOREIGN KEY ("B") REFERENCES "books" ("booksId") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO "new__AuthorsToBooks" ("A", "B") SELECT "A", "B" FROM "_AuthorsToBooks";
DROP TABLE "_AuthorsToBooks";
ALTER TABLE "new__AuthorsToBooks" RENAME TO "_AuthorsToBooks";
CREATE UNIQUE INDEX "_AuthorsToBooks_AB_unique" ON "_AuthorsToBooks"("A", "B");
CREATE INDEX "_AuthorsToBooks_B_index" ON "_AuthorsToBooks"("B");
CREATE TABLE "new__BooksToGenres" (
    "A" INTEGER NOT NULL,
    "B" INTEGER NOT NULL,
    CONSTRAINT "_BooksToGenres_A_fkey" FOREIGN KEY ("A") REFERENCES "books" ("booksId") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_BooksToGenres_B_fkey" FOREIGN KEY ("B") REFERENCES "genres" ("genreId") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO "new__BooksToGenres" ("A", "B") SELECT "A", "B" FROM "_BooksToGenres";
DROP TABLE "_BooksToGenres";
ALTER TABLE "new__BooksToGenres" RENAME TO "_BooksToGenres";
CREATE UNIQUE INDEX "_BooksToGenres_AB_unique" ON "_BooksToGenres"("A", "B");
CREATE INDEX "_BooksToGenres_B_index" ON "_BooksToGenres"("B");
CREATE TABLE "new_authors" (
    "authorId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "registerDate" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "new_authors" ("authorId", "name", "registerDate") SELECT "authorId", "name", "registerDate" FROM "authors";
DROP TABLE "authors";
ALTER TABLE "new_authors" RENAME TO "authors";
CREATE TABLE "new_books" (
    "booksId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "publisher" TEXT NOT NULL,
    "publish_date" DATETIME NOT NULL,
    "registered_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "new_books" ("booksId", "name", "publish_date", "publisher", "registered_at") SELECT "booksId", "name", "publish_date", "publisher", "registered_at" FROM "books";
DROP TABLE "books";
ALTER TABLE "new_books" RENAME TO "books";
CREATE TABLE "new_genres" (
    "genreId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "genre" TEXT NOT NULL,
    "registerDate" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "new_genres" ("genre", "genreId", "registerDate") SELECT "genre", "genreId", "registerDate" FROM "genres";
DROP TABLE "genres";
ALTER TABLE "new_genres" RENAME TO "genres";
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;
