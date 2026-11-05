// stone:job stone:math.map_range
// stone:function map_range_rs

#[no_mangle]
pub extern "C" fn map_range_rs(value: i32, in_min: i32, in_max: i32, out_min: i32, out_max: i32) -> i32 {
    if in_max == in_min {
        return out_min;
    }
    let t = (value - in_min) as f64 / (in_max - in_min) as f64;
    (out_min as f64 + (out_max - out_min) as f64 * t) as i32
}
