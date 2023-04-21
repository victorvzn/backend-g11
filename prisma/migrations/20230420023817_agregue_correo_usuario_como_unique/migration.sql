/*
  Warnings:

  - The primary key for the `items_carrito` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - A unique constraint covering the columns `[correo]` on the table `usuarios` will be added. If there are existing duplicate values, this will fail.

*/
-- AlterTable
ALTER TABLE "items_carrito" DROP CONSTRAINT "items_carrito_pkey",
ADD COLUMN     "id" SERIAL NOT NULL,
ADD CONSTRAINT "items_carrito_pkey" PRIMARY KEY ("id");

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_correo_key" ON "usuarios"("correo");
