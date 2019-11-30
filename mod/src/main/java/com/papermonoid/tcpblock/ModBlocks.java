package com.papermonoid.tcpblock;

import net.minecraft.tileentity.TileEntityType;
import net.minecraftforge.registries.ObjectHolder;

public class ModBlocks {
	@ObjectHolder("tcpblock:receiver_block")
	public static ReceiverBlock RECEIVER_BLOCK;
	
    @ObjectHolder("tcpblock:receiver_block")
    public static TileEntityType<ReceiverTile> RECEIVER_TILE;
}
