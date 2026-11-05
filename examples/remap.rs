// stone:job stone:math.remap
// stone:function remap_rs

#[no_mangle]
pub extern "C" fn remap_rs(x: i32, in_min: i32, in_max: i32, out_min: i32, out_max: i32) -> i32 {
    let t = (x - in_min) as f64 / (in_max - in_min) as f64;
    (out_min as f64 + (out_max - out_min) as f64 * t) as i32
}
