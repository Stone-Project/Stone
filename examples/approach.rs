// stone:job stone:math.approach
// stone:function approach_rs

#[no_mangle]
pub extern "C" fn approach_rs(current: i32, target: i32, mut step: i32) -> i32 {
    if step < 0 {
        step = -step;
    }
    if current < target {
        let next_value = current + step;
        if next_value > target {
            return target;
        }
        return next_value;
    }
    let next_value = current - step;
    if next_value < target {
        return target;
    }
    next_value
}
