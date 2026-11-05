// stone:job stone:math.floor
// stone:function floor_rs

#[no_mangle]
pub extern "C" fn floor_rs(x: f64) -> f64 {
    x.floor()
}
