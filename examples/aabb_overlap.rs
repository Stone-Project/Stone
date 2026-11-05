// stone:job stone:physics.aabb_overlap
// stone:function aabb_overlap_rs

#[no_mangle]
pub extern "C" fn aabb_overlap_rs(ax: i32, ay: i32, aw: i32, ah: i32, bx: i32, by: i32, bw: i32, bh: i32) -> bool {
    ax < bx + bw && ax + aw > bx && ay < by + bh && ay + ah > by
}
